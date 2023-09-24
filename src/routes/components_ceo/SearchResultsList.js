import "./SearchResultsList.css";
import { SearchResult } from "./SearchResult";

export const SearchResultsList = ({ results, setSelectedResult, setInput, setKuken }) => {
  return (
    <div className="results-list">
      {results.map((result, id) => {
        return <SearchResult result={result} key={id} setSelectedResult={setSelectedResult} setInput={setInput} setKuken={setKuken}/>;
      })}
    </div>
  );
};