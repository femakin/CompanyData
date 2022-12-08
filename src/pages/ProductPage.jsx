import React from 'react'
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import config from '../config';
import Header from '../components/Header';
import SearchInput from '../components/SearchInput';
import Hero from '../components/Hero';
import Category from '../components/Category';
import Footer from '../components/Footer';
import ProductIccon from '../components/ProductIccon';


function ProductPage() {
    let { category } = useParams();
    let [items, setItems] = useState([]);

    useEffect(() => {
        const getItems = async () => {
            let items = await fetch(`${config.BASE_URL}/items/category/${category}`).then(r => r.json());
            setItems(items);

        }
        getItems();
    }, [category]);

    return (
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

                        <Hero />
                    </div>

                    <div className="category_container">

                        <ProductIccon item={items} />
                    </div>
                </main>
                <Footer />
            </div>
        </div>
    )
}

export default ProductPage