import React from "react";
import { FaPhone, FaEnvelope, FaMapMarker } from "react-icons/fa";
import "./Contact.css";

function Contact() {
  return (
    <div className="contact">
      <div className="contact-container">
        <div className="contact-info">
          <h1>Spørsmål/Kontakt</h1>
          <p>
            Kontakt meg på:
          </p>
          <div className="contact-details">
            <div className="contact-item">
              <FaPhone className="contact-icon" />
              <p>......</p>
            </div>
            <div className="contact-item">
              <FaEnvelope className="contact-icon" />
              <p className="kuk">Sondrenils1@outlook.com</p>
            </div>
            <div className="contact-item">
              <FaMapMarker className="contact-icon" />
              <p>Bergen</p>
            </div>
          </div>
        </div>
        <div className="contact-form">
          <h2>Send en melding</h2>
          <form>
            <div className="form-group">
              <label htmlFor="name">Navn</label>
              <textarea type="text" id="name" name="name" required />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <textarea type="email" id="email" name="email" required />
            </div>
            <div className="form-group">
              <label htmlFor="message">Melding</label>
              <textarea id="message" name="message" required></textarea>
            </div>
            <button type="submit">Send</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Contact;
