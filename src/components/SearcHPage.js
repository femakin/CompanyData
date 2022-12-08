import React, { useContext, useEffect, useState } from 'react'
import { useLocation, useParams } from 'react-router-dom';
import config from "../config.js";
import { AllContext } from '../context/FormContext.jsx';
import Footer from './Footer.js';
import Header from './Header.js';
import Hero from './Hero.js';
import ProductIccon from './ProductIccon.js';
import SearchInput from './SearchInput.js';

export default function SearcHPage() {
    let { query } = useParams();
    let [items, setItems] = useState([]);
    const { setUsers, users } = useContext(AllContext);
    const { location } = useLocation();





    useEffect(() => {
        console.log(config.BASE_URL, 'config.BASE_URL')
        if (!query) return;
        fetch(`${config.BASE_URL}/search/${query}`).then(r => r.json()).then(d => {
            setItems(d);
            console.log(d, 'ddddd')
        });

        console.log(location?.state, 'location.state')
    }, [query])




    return (
        <div>

            <div className="home_container">
                <div className="App container-fluid">
                    <header className="App-header">
                        <Header />
                    </header>
                    <main>
                        <div className="searchcontainer">
                            <SearchInput />
                        </div>
                        <div className="row justify-content-center">
                            {/* <h1>Main Body</h1> */}
                            <Hero />
                        </div>

                        <div className="category_container">
                            {/* <h1>Main Body</h1> */}
                            {/* <Category /> */}
                            <ProductIccon item={items} />
                        </div>
                    </main>
                    <Footer />
                </div>
            </div>



        </div>
    )
}
