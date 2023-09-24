import { FaSearch } from "react-icons/fa";
import "./SearchBar.css";

export const SearchBar = ({ setResults, input, setInput, setKuken }) => {
  const fetchData = async (value) => {
    try {
      const response = await fetch(`https://dumbstockapi.com/stock?exchanges=NYSE`);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();

      const results = data.filter((item) => {
        return (
          value &&
          item &&
          item["ticker"] &&
          item["name"]
        );
      });
      setResults(results);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleChange = (value) => {
    setInput(value);
    fetchData(value);
    setKuken(true);
  };

  return (
    <div className="input-wrapper">
      <FaSearch id="search-icon" />
      <input
        placeholder="Type to search..."
        value={input.company}
        onChange={(e) => handleChange(e.target.value)}
        onClick={() => setKuken(false)}
      />
    </div>
  );
};
