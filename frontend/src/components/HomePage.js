import React, { useEffect } from 'react';
import { Grid,
	Button,
	Typography,
	
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { useHistory } from 'react-router-dom';

const useStyles = makeStyles({ 

	root: { 

		background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
		borderRadius: 3,
		border: 0, 
		color: 'white',
		height: 100,
		width:  250,
		padding: '0 30px',
		boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',

	}, 

	

});


const HomePage=()=>{

	const classes = useStyles();
	const history = useHistory();

	useEffect(()=>{

		//wait for session to be updated at backend
		setTimeout(()=>{

		fetch('/api/UserInRoom')
		.then(res=>res.json())
		.then(data=>{

			alert(data.code);


			

			if (data.code!==null){
				history.push('/GetRoom/'+data.code);
			} 

				
			

			


		})




		},100)

	},[])
	
	
	return(
		<Grid  container>

		<Grid justifyContent="center" alignItems="center" container item>

		<Typography variant="h3"> MUSIC CONTROLLER </Typography>

		</Grid>

		<Grid spacing={2} justifyContent="space-around" alignItems="center" item container>


			<Grid item>
				<Button classes={{root:classes.root}}  variant="container" onClick={()=>history.push('CreateRoom')}> Create Room</Button>

			</Grid>

			<Grid item>

				<Button classes={{root:classes.root}} size="large" variant="contained" onClick={()=>history.push('JoinRoom')}> Join Room </Button>
			</Grid>


		</Grid>

		</Grid>

	

	);


}

export default HomePage;
