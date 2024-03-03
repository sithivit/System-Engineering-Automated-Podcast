import NavigationBar from './components/NavigationBar.js'
import IndexMain from './components/IndexMain.js';
import HomeMain from './components/HomeMain.js';
import EpisodesMain from './components/EpisodesMain.js';
import CreateMain from './components/CreateMain.js';
import SignIn from './components/SignIn.js';

export function Login() {
  return (
    <div className="Login">
      <NavigationBar />
      <SignIn />
    </div>
  )
}

export function Home() {
  return (
    <div className="Home">
      <NavigationBar />
      <HomeMain />
    </div>
  )
}

export function Episodes() {
  return (
    <div className="Episodes">
      <NavigationBar />
      <EpisodesMain />
    </div>
  )
}

export function Create() {
  return (
    <div className="Create">
      <NavigationBar />
      <CreateMain />
    </div>
  )
}

export function App() {
  return (
    <div className="App">
      <NavigationBar />
      <IndexMain />
    </div>
  );
}
