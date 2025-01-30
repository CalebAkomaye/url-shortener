import Container from "./components/container";
import Footer from "./components/footer";
import Intro from "./components/intro";
import Navbar from "./components/navabar";

function App() {
  return (
    <>
      <Navbar />
      <Container>
        <Intro />
      </Container>
      <Footer />
    </>
  );
}

export default App;
