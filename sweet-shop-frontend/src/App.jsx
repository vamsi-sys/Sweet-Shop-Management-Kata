import Login from "./Login";
import Dashboard from "./Dashboard";

function App() {
  const token = localStorage.getItem("token");

  return (
    <div style={{ height: "100vh", margin: 0 }}>
      {!token ? <Login /> : <Dashboard />}
    </div>
  );
}

export default App;
