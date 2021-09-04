import React from 'react';
import { render} from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import HomePage from "./HomePage";
import CreateRoomPage from "./CreateRoomPage";
import GetRoomPage from "./GetRoomPage";
import JoinRoomPage from "./JoinRoomPage";

const App=()=>{


	


		return(
			

			<Router>
				<Switch>
			

					<Route exact path="/">
						<HomePage/>

					</Route>
					<Route path="/CreateRoom">
						<CreateRoomPage/>
					</Route>

					<Route path="/GetRoom/:code">


						<GetRoomPage/>

					</Route>
					<Route path='/JoinRoom'>

						<JoinRoomPage/>
					</Route>

				</Switch>

			</Router>
		
		);

	


};

export default App;

//find div with id "app"
const appDiv = document.getElementById('app');

//render in the div
render(<App/>,appDiv);
