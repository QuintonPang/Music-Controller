import React, { useEffect, useState } from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import SkipPreviousIcon from '@material-ui/icons/SkipPrevious';
import PlayArrowIcon from '@material-ui/icons/PlayArrow';
import SkipNextIcon from '@material-ui/icons/SkipNext';
import LinearProgress from '@material-ui/core/LinearProgress';
import PauseIcon from '@material-ui/icons/Pause';

const useStyles = makeStyles((theme) => ({
	  root: {
		      display: 'flex',
		    },
	  details: {
		      display: 'flex',
		      flexDirection: 'column',
		    },
	  content: {
		      flex: '1 0 auto',
		    },
	  cover: {
		      width: 151,
		    },
	  controls: {
		      display: 'flex',
		      alignItems: 'center',
		      paddingLeft: theme.spacing(1),
		      paddingBottom: theme.spacing(1),
		    },
	  playOrPauseIcon: {
		      height: 38,
		      width: 38,
		    },
}));

const MusicPlayer=() =>{

	  const classes = useStyles();
	  const theme = useTheme();
	  const [ songData, setSongData ] = useState({});
          const { progress, image, duration, is_playing, song_id, artists, song_name,votes_to_skip, current_votes } = songData;
	  const [ pause, setPause ] = useState(false);
	  const songProgress = progress/duration *100

	  const handlePlayPause = () =>{

		setPause(!pause)

		if(pause===true){
			
			const requestOptions={

				method:"PUT",
				headers:{"Content-Type":"application/json"},

			}

			fetch('/spotify/PlaySong',requestOptions);


		}else{

			const requestOptions={

				method:"PUT",
				headers:{"Content-Type":"application/json"},

			}

			fetch('/spotify/PauseSong',requestOptions);


			


		}


	  }

	const handleSkip=()=>{

			
			
		const requestOptions={

			
			method:"POST",
			
			headers:{"Content-Type":"application/json"},

		
		}

		
		fetch('/spotify/SkipSong',requestOptions);



	}
	
	  useEffect(()=>{

		const handleSongData=setInterval(()=>{
		fetch('/spotify/CurrentSong').then(res=>res.json()).then(data=>setSongData(data));
		},1000);
		
		  return ()=>{clearInterval(handleSongData)};



	  },[songData]);



	  return (
		      <Card className={classes.root}>
		        <div className={classes.details}>
		          <CardContent className={classes.content}>
		            <Typography component="h5" variant="h5">
		  		{song_name}
		            </Typography>
		            <Typography variant="subtitle1" color="textSecondary">
		  		{artists}
		            </Typography>

		            <Typography variant="subtitle1" color="textSecondary">
				  Votes To Skip:{current_votes}/{votes_to_skip}
		            </Typography>

		  	<Typography varianr="subtitile1" color="textSecondary">

		  		{String(Math.floor(progress/60000))+":"+String(progress%60000)}/{String(Math.floor(duration/60000))+":"+String(duration%60000)}
		  	</Typography>
			  <LinearProgress variant="determinate" value={songProgress}/>
		          </CardContent>
		          <div className={classes.controls}>
		            <IconButton aria-label="previous">
		              {theme.direction === 'rtl' ? <SkipNextIcon /> : <SkipPreviousIcon />}
		            </IconButton>
		            <IconButton onClick={()=>handlePlayPause()} aria-label="play/pause">
		  {pause?<PlayArrowIcon className={classes.playOrPauseIcon} />:<PauseIcon className={classes.playOrPauseIcon} />}
			    </IconButton>
		            <IconButton onClick={()=>handleSkip()}  aria-label="next">
		              {theme.direction === 'rtl' ? <SkipPreviousIcon /> : <SkipNextIcon />}
		            </IconButton>
		          </div>
		        </div>
		        <CardMedia
		          className={classes.cover}
		          image={image}
		          title={song_name+" cover"}
		        />
		      </Card>
		    );
}

export default MusicPlayer;
