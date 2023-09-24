import React from "react";
import "./About.css";

function About() {
  return (
    <div className="about">
      <div className="about-content">
        <h1>About Me</h1>
        <p>
          Halla! Jeg er en 22 år gammel IT og økonomistudent ved Universitetet i Bergen
        </p>
        <p>
          
        </p>
        <p>
          Denne siden vil bli brukt til å vise prosjekter jeg holder på med 
          og sikkert litt tull
        </p>
      </div>
      <div className="about-image">
        <img
          src="https://www.fintechenigma.no/img/Sondre.jpeg"
          alt="Your Image"
            />
      </div> 
    </div>
  );
}

export default About;
