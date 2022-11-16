import React from 'react'
import Header from '../components/Header'
import Hero from '../components/Hero'
import SearchInput from '../components/SearchInput'
import '../index.css'

function Home() {
    return (
        <div className='home_container' >
            <div className="App container-fluid">
                <header className="App-header">
                    <Header />
                </header>
                <main>
                    <div className="row justify-content-center">
                        {/* <h1>Main Body</h1> */}
                        <Hero />
                    </div>


                    <div className='searchcontainer' >

                        <SearchInput />
                    </div>
                </main>
                <footer>
                    <h1>Footer</h1>
                </footer>
            </div>
        </div>
    )
}

export default Home