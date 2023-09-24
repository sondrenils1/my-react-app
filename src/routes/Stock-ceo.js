import { useState } from "react";

import "./Stock-ceo.css";
import { SearchBar } from "./components_ceo/SearchBar";
import { SearchResultsList } from "./components_ceo/SearchResultsList";
//import bilde from "./business.jpg"





function Stock_ceo() {
  const [results, setResults] = useState([]);
  const [selectedResult, setSelectedResult] = useState("");
  const [input, setInput] = useState("");
  const [kuken, setKuken] = useState(false);





// images\Anders_Opedal_equinor\Anders Opedal equinor_3.jpeg

  return (
    <div className="App">
      <h1 className="h1">
        OSLO BØRS CEO SØK
      </h1>
      <div className="search-bar-container">
        <SearchBar setResults={setResults} input={input} setInput={setInput} setKuken={setKuken}/>
        {results && results.length > 0 && kuken===true && <SearchResultsList results={results} setSelectedResult={setSelectedResult} setInput={setInput} setKuken={setKuken}/>}
      </div>
      <div className="selected-result-container">
        {kuken === false && <img src={selectedResult} left = "80%" alt=""/>}
      </div>
      <div className="hoi">
      {kuken === false && input.name}
      </div>
    </div>
  );
}


export default Stock_ceo;