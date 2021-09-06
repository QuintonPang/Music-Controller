import React,{ useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';
import { Grid, Button, Typography, LinearProgress } from '@material-ui/core';
import { Formik, Form, Field } from 'formik';      
import { TextField, CheckboxWithLabel } from 'formik-material-ui';
import MusicPlayer from './MusicPlayer';

const GetRoomPage = ()=>{

	const { code } = useParams();
	const [ roomData,setRoomData ] = useState({}); 
	const { id, host, skipVotes, guestCanPause, timeCreated, isHost} = roomData;
	const [ settings, setSettings ] = useState(false);
	const [ isAuthenticated, setIsAuthenticated ] = useState(false);

	const history = useHistory();

	const handleLeaveRoom = () =>{


		const requestOptions = {

			method:"POST",


			headers:{ "Content-Type": "application/json"},




		};


		fetch('/api/UserLeaveRoom',requestOptions)
		.then(history.push('/'));
		


	};

	useEffect(()=>{



		fetch('/api/GetRoomView?code='+code).then(response=>response.json()).then(data=>{


		setRoomData(data); 
		
		data.isHost&&( //if user is the host                                                                                                                           
			fetch('/spotify/IsAuthenticated')  //check if authenticated
			                       
			.then(res=>res.json())
			                       
			.then(data=>{

							                                                                                 
							                                                      		                                                         
				setIsAuthenticated(data.status)
							                               
				if (!data.status){    //if not authenticated
												                                      
					fetch('/spotify/GetAuthUrl')  //authenticate
												                                       
						
					.then(res=>res.json())
																	                                      
					.then(data=>window.location.replace(data.url))}}))                                                                                                       






																						                        });

			

			

			


		

		


		

	},[settings]);


	return(

	
		settings?(

			

			<Grid>

			<Typography variant="h3">Setting</Typography>

			<Formik
			


			                
			initialValues={{

						                       
				skipVotes:{skipVotes},
				guestCanPause:false,	
					


						
			}}


			                
			onSubmit={(values, { setSubmitting }) => {
				
				                                                                                                                                                
				setSubmitting(false);
				


                                //send data to backend

                                const requestOptions = {



                                        method: "PATCH",


                                        headers: {


                                                "Content-Type": "application/json"



                                        },





                                        //json.stringify second parameter is replace, third parameter is spacing beteween keys






					body: JSON.stringify({...values,code:code},null,2),




                                };






                                fetch("/api/UpdateRoomView",requestOptions) //post data in /api/JoinRoomView




                                .then((response)=>{


                                                if(response.ok){
                                                        alert("Updated successfully");

                                                }else{


                                                        alert("Failed to update");
                                                }




                                        })		
				

						
					
				
			}}>
										                                                                                                                                                                     					                                                                                                                                                                                                                                                  
			
			{({ submitForm, isSubmitting }) => (	                                                                                                                                                                                                                                                                                                                                                                                     
							<Grid container justifyContent="center" alignItems="center">
							                                                                                                                                                                                                                             
							<Form>
				
						
										                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   					
							<Grid container item style={{padding:20,backgroundColor:"#e3e4e6"}} justifyContent="center">
										                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
								<Grid container item spacing={2} justifyContent="center" xs={10}>

									<Grid item>
			                       
						<Field
			                          component={CheckboxWithLabel}
			                          type="checkbox"
			                          name="guestCanPause"                                                             Label={{ label: 'Allow guest to pause music' }}
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

			                        Update

			                        </Button>

						<Button
						variant="contained"
						color="red"
						disabled={isSubmitting}
						onClick={()=>setSettings(false)}
						>
						Close
						</Button>
			                                                    
									</Grid>

			                      
					
								</Grid>
			                                                                                                       
			
							</Grid>
	
			                  
							</Form>

			                      
						</Grid>
			        
				                                                             
			
			)}


         
					</Formik>


		
					
	
			</Grid>
			

			



		):(<Grid container alignItems="center" direction="column">


			<h1> Id: {id}</h1>
			<p> Code: {code} </p>
			<p> Votes to skip music: {skipVotes} </p>
			<p> Can guest pause: {String(guestCanPause).toUpperCase()} </p>
			<p> Time Created: {timeCreated} </p>


			<p> Are you a host: {String(isHost).toUpperCase()} </p>
			<p> Connected to Spotfiy: {String(isAuthenticated).toUpperCase()}</p>

			<MusicPlayer/>
			<Button onClick={()=>handleLeaveRoom()} variant='contained'>Leave Room </Button>
			<Button onClick={()=>setSettings(true)} variant="contained">Settings</Button>

		</Grid>)
		
	);


};


export default GetRoomPage;
