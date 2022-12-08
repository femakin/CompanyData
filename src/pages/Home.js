import React from "react";
import Category from "../components/Category";
import Footer from "../components/Footer";
import Header from "../components/Header";
import Hero from "../components/Hero";
import SearchInput from "../components/SearchInput";
import "../index.css";


function Home() {
  return (

    <div className="home_container">
      <div className="App container-fluid">
        <header className="App-header">
          <Header />
        </header>
        <main>
          <div className="searchcontainer">

          </div>
          <div className="row justify-content-center">
            {/* <h1>Main Body</h1> */}
            <Hero />
          </div>

          <div className="category_container">
            {/* <h1>Main Body</h1> */}
            <Category />
          </div>
        </main>
        <Footer />
      </div>
    </div>
  );
}

export default Home;
