import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";
import { FcRadarPlot } from "react-icons/fc";
import { FaBars, FaTimes } from "react-icons/fa";
import { IconContext } from "react-icons/lib";
import { NavLink } from "react-router-dom";
import { AiOutlineMail } from "react-icons/ai";
import { AiOutlineHome } from "react-icons/ai";
import { BsNewspaper } from "react-icons/bs";

function Navbar() {
  const [click, setClick] = useState(false);

  const handleClick = () => setClick(!click);
  const closeMobileMenu = () => setClick(false);

  return (
    <>
      <IconContext.Provider value={{ color: "#fff" }}>
        <nav className="navbar">
          <div className="navbar-container container">
            <Link to="/" className="navbar-logo" onClick={closeMobileMenu}>
              <FcRadarPlot className="navbar-icon" />
              Sondres Playground
            </Link>
            <div className="menu-icon" onClick={handleClick}>
              {click ? <FaTimes /> : <FaBars />}
            </div>
            <ul className={click ? "nav-menu active" : "nav-menu"}>
              <li className="nav-item">
                <NavLink
                  to="/"
                  className={({ isActive }) =>
                    "nav-links" + (isActive ? " activated" : "")
                  }
                  onClick={closeMobileMenu}
                >
                  Home
                  <AiOutlineHome className="page-icon" />
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  to="/stocky-prices"
                  className={({ isActive }) =>
                    "nav-links" + (isActive ? " activated" : "")
                  }
                  onClick={closeMobileMenu}
                >
                  Stock-price
                  <AiOutlineHome className="page-icon" />
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  to="/stock-ceo"
                  className={({ isActive }) =>
                    "nav-links" + (isActive ? " activated" : "")
                  }
                  onClick={closeMobileMenu}
                >
                  Stock-ceo
                <AiOutlineMail className="page-icon" />
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  to="/about"
                  className={({ isActive }) =>
                    "nav-links" + (isActive ? " activated" : "")
                  }
                  onClick={closeMobileMenu}
                >
                  About
                <BsNewspaper className="page-icon" />
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  to="/contact"
                  className={({ isActive }) =>
                    "nav-links" + (isActive ? " activated" : "")
                  }
                  onClick={closeMobileMenu}
                >
                  Contact
                <AiOutlineMail className="page-icon" />
                </NavLink>
              </li>
            </ul>
          </div>
        </nav>
      </IconContext.Provider>
    </>
  );
}

export default Navbar;
