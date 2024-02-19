import NavigationBar from './components/NavigationBar.js'
import IndexMain from './components/IndexMain.js';
import HomeMain from './components/HomeMain.js';
import CategoriesMain from './components/CategoriesMain.js';
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

export function Categories() {
  return (
    <div className="Categories">
      <NavigationBar />
      <CategoriesMain />
    </div>
  )
}

export function Create() {
  return (
    <div className="Create">
      <NavigationBar />
      <h1>Create</h1>
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
