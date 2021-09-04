import React from 'react';
import { Formik, Form, Field } from 'formik'; 
import { Button, LinearProgress } from '@material-ui/core';
import { TextField } from 'formik-material-ui';
import { useHistory } from 'react-router-dom';

const JoinRoomPage = ()=>{


	const history = useHistory();




	return(
		


	
		
			     
			<Formik
			       
			initialValues={{
					        
				code:'',
						        

				
			
			}}
			     
			validate={values => {
					      
				const errors={}
					      
				if (!values.code) {

							          

					errors.code = 'Required';
					
				} 

									      
					
									        		
				return errors;
				

			}}
			      

			onSubmit={(values,{ setStatus, resetForm, setSubmitting}) => {
					     

				setTimeout(() => {
							          
					setSubmitting(false);
							          
					const requestOptions={
						method:"POST",
						headers:{

							"Content-Type":"application/json"
						},
						body: JSON.stringify(values),
					}

					fetch('/api/JoinRoomView',requestOptions)
					.then(response=>{

						if (response.ok){ //if valid
							history.push('/getRoom/'+values.code)
						}else{
							alert("Room unavailable");
						
													
							resetForm();
					
						}
						

					})			
		
				}, 500);
					   
			}}
			      >
			      
			{({ submitForm, isSubmitting }) => (
					 
				<Form>
					  
				<Field
					    
				component={TextField}
					           
				name="code"
				
							
				
				label="Code"
					          />
					          {isSubmitting && <LinearProgress />}
					       
				<br />
					     
				<Button
					     
				variant="contained"
					     
				color="primary"
					    
				disabled={isSubmitting}
					   
				onClick={submitForm}
					     
				>
					      
				Join
					  
				</Button>
				
				</Form>
			
			)}

			   

			</Formik>
		
	);			
		


}







export default JoinRoomPage;
