import * as React from 'react';

import { Formik, Form, Field } from 'formik';

import { Button, LinearProgress, Grid } from '@material-ui/core';

import { TextField, CheckboxWithLabel } from 'formik-material-ui';

import { useHistory } from 'react-router-dom';



const CreateRoomPage = () =>{

	const history= useHistory();

	return (
		

		<Formik

			

		initialValues={{

			skipVotes:2,
			guestCanPause:false,

		}}


		onSubmit={(values, { setStatus,resetForm, setSubmitting }) => {

			setTimeout(() => {

				setSubmitting(false);

				//send data to backend
				const requestOptions = { 
					method: "POST", 
					headers: { 
						"Content-Type": "application/json"
					},

					//json.stringify second parameter is replace, third parameter is spacing beteween keys

					body: JSON.stringify(values,null,2),
				};

				fetch("/api/CreateRoomView",requestOptions) //post data in /api/CreateRoomView
				.then((response)=>response.json()) //make it a json formati
				.then(data=>{

					alert("Created Succesfully with host "+data.host);
					history.push('/');

				}


				); //alert json data

				//reset form
				resetForm();
			}, 500);

		}}

		>

		{({ submitForm, isSubmitting }) => (

			<Grid container justifyContent="center" alignItems="center">

			<Form>
			
			<Grid container item style={{padding:20,backgroundColor:"#e3e4e6"}} justifyContent="center">
			<Grid container item spacing={2} justifyContent="center" xs={10}>
		

			<Grid item>
			<Field
			  component={CheckboxWithLabel}
			  type="checkbox"
			  name="guestCanPause"
			  Label={{ label: 'Allow guest to pause music' }}
			/>

			<br/>

			<Field

			component={TextField}

			type="number"

			label="Number of votes to skip music"

			name="skipVotes"


			/>
			</Grid>

			

			{isSubmitting && <LinearProgress />}
			
			<br />


			
			<Grid item>

			<Button

			variant="contained"

			color="primary"

			disabled={isSubmitting}

			onClick={submitForm}

			>

			Submit

			</Button>

			</Grid>

			</Grid>

			</Grid>

			</Form>

			</Grid>
		)}

		</Formik>

		

	);

}

export default CreateRoomPage;

