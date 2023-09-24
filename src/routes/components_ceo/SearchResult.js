import React from "react";
import "./SearchResult.css";


export const SearchResult = ({ result, setSelectedResult, setInput, setKuken}) => {

  let onClickk = (result, setSelectedResult) => {
    const navn = result.name;
    const nytt_navn = navn.replace(/ /g, "_");
    const firma = result.company;
    const nytt_firma = firma.toLowerCase();
    try {
      if (nytt_firma.includes(" ")) {
      const nytt_firma1 = nytt_firma.replace(/ /g, "_");
      setSelectedResult(require(`./images/${nytt_navn}_${nytt_firma1}/${navn} ${nytt_firma}_3.jpeg`))
      } else { 
      setSelectedResult(require(`./images/${nytt_navn}_${nytt_firma}/${navn} ${nytt_firma}_3.jpeg`));
      }
    } catch(error) {
      if (nytt_firma.includes(" ")) {
        const nytt_firma1 = nytt_firma.replace(/ /g, "_");
        setSelectedResult(require(`./images/${nytt_navn}_${nytt_firma1}/${navn} ${nytt_firma}_3.png`))
        } else { 
        setSelectedResult(require(`./images/${nytt_navn}_${nytt_firma}/${navn} ${nytt_firma}_3.png`));
        }
    }

    
    //setSelectedResult(require(`${process.env.PUBLIC_URL}/images/${nytt_navn}_${nytt_firma}/${navn} ${nytt_firma}_3.jpeg`));
    setInput(result);
    setKuken(false);
  }
  
  //images\Herman_Bilung_2020_bulkers\Herman Bilung 2020 bulkers_3.jpeg
  
  //images\Anders_Opedal_equinor\Anders Opedal equinor_2.png
  
  return (
    <div
      className="search-result"
      onClick={() => onClickk(result, setSelectedResult)}
    >
      {result.company}
    </div>
  );
};
