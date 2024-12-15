import React from "react";

import './styles/footer.css'
import Tg from './icon/tg.png';

const Footer = () => {
    return (
        <div className="footer-main-container">
            <div className="footer-num-tg-container">
                <h3 className="footer-num">+7-8352-20-12-09</h3>
                <img src={Tg} alt="Tg" className="footer-tg-icon" />
            </div>
            <h3 className="text-silant">Мой Силант</h3>
        </div>
    );
};

export default Footer;