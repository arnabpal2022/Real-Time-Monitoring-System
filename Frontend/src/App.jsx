import "./App.css";
import services from "./services/services";

function App() {
  const handleExplore = async () => {
    try {
      const response = await services.produceEventToExploreTopic();
      console.log("Explore Submitted");
    } catch (error) {
      console.error("Error: sending Explore Click Event", error);
    }
  };

  const handleBuy = async () => {
    try {
      const response = await services.produceEventToBuyTopic();
      console.log("Buy Submitted");
    } catch (error) {
      console.error("Error: sending Buy Click Event", error);
    }
  };

  return (
    <>
      <div className="App">
        <div>
          <h1>Kafka Producer</h1>
          <br />
          <button onClick={handleExplore}>Enroll Now</button> <br/> <br/>
          <button onClick={handleBuy}>Buy Now</button>
        </div>
      </div>
    </>
  );
}

export default App;
