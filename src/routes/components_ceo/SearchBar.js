import { FaSearch } from "react-icons/fa";

import "./SearchBar.css";
import Ceo_json from "./Ceo_list.json"; // Import the local JSON file

export const SearchBar = ({ setResults, input, setInput, setKuken}) => {

  const fetchData = (value) => {
    const results = Ceo_json.filter((ceo) => {
      return (
        value &&
        ceo &&
        ceo["company"] &&
        ceo["company"].toLowerCase().includes(value.toLowerCase()) // Filter by company name
      );
    });
    setResults(results);
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

