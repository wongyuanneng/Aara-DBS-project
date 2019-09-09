import React, { Component } from 'react';
// import logo from './logo.svg';
// import './App.css';

import Amplify, { Interactions } from 'aws-amplify';
import { ChatBot, AmplifyTheme } from 'aws-amplify-react';
import awsconfig from './aws-exports';
// import Button from 'react-bootstrap/Button';

Amplify.configure(awsconfig);

// Imported default theme can be customized by overloading attributes
const myTheme = {
  ...AmplifyTheme,
  sectionHeader: {
    ...AmplifyTheme.sectionHeader,
    backgroundColor: '#ff6600'
  }
};

class App extends Component {

  handleComplete(err, confirmation) {
    if (err) {
      alert('Bot conversation failed')
      return;
    }

    alert('Success: ' + JSON.stringify(confirmation, null, 2));
    return '- Terminated -';
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Welcome to ChatBot Demo</h1>
        </header>
        <ChatBot
          title="My Bot"
          theme={myTheme}
          botName="BookTrip_test"
          welcomeMessage="Hi there! Would you like to participate in a demo program for maximizing your quality of life?"
          onComplete={this.handleComplete.bind(this)}
          clearOnComplete={true}
          conversationModeOn={false}
        />
      </div>
    );
  }
}

// class App extends Component {
//   testSend = async () => {
//     let userInput = "I want to reserve a hotel for tonight";

//     // Provide a bot name and user input
//     const response = await Interactions.send("BookTrip_test", userInput);
    
//     // Log chatbot response
//     console.log (response.message);
//   } 
//   render() {
//     return (
//       <div className="App">
//         <div className="App-header">
//           <img src={logo} className="App-logo" alt="logo" />
//           <h2>Welcome to React</h2>
//         </div>
//         <p className="App-intro">
//           To get started, edit <code>src/App.js</code> and save to reload.
//         </p>
//         <Button 
//         variant="primary"
//         onClick={this.testSend}
//         >
//           Test send to chatbot
//         </Button>
//       </div>
//     );
//   }
// }

export default App;
