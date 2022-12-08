import React, { useContext, useEffect, useState } from 'react'
import './SearchInput.css'
import { Link, useNavigate } from "react-router-dom";
import config from '../config';
import { AllContext } from '../context/FormContext.jsx'

function SearchInput() {
    let [suggestions, setSuggestions] = useState([]);
    let [query, setQuery] = useState("");
    let [datal, setDataL] = useState()

    const navigate = useNavigate();
    const { setUsers, users } = useContext(AllContext);




    const handleSearchButton = async (e) => {
        e.preventDefault();
        // history.push(`/search/${query}`);
        console.log(query, 'queryyy')
        navigate(`/search/${query}`, {
            state: users
        });

    }

    const handleSearchTermChange = (e) => {
        e.preventDefault();
        setQuery(e.target.value);
    }

    const handleKeyUp = async (e) => {
        e.preventDefault();
        let result = await fetch(`${config.BASE_URL}/autocomplete/${query}`).then(r => r.json());
        setSuggestions(result);
        setQuery(e?.target?.value)
        console.log(result, 'resultttt')
        // console.log(e?.target?.value, 'search field')
        setDataL(result, 'resultttt twoooo')
        setUsers(e?.target?.value)
        // console.log(query, 'query')
        navigate(`/search/${query}`, {
            state: query
        });
    }



    // useEffect(() => {
    //     handleSearchButton()
    // }, [query]);





    return (
        <div>




            <form className="p-4" onSubmit={handleSearchButton}>
                <div className='form_bdy' >

                    <div className='' >

                        <input value={query} onKeyUp={handleKeyUp} onChange={handleSearchTermChange} className="form-control" list="datalistOptions" placeholder="What are you looking for?" />

                        <datalist id="datalistOptions">
                            {suggestions?.map((s, index) => {
                                return (
                                    <select   >
                                        <option key={index} value={s.name} />
                                    </select>

                                )
                            })}
                        </datalist>
                    </div>
                    <div className='form_two' >

                        <button type="button" onClick={handleSearchButton} className="btn btn-secondary">Search</button>


                    </div>

                </div>
            </form>


            {/* <form className="p-4" onSubmit={handleSearchButton}>
                <div className="form_bdy">
                    <div className="">
                        <input
                            value={query}
                            onKeyUp={handleKeyUp}
                            onChange={handleSearchTermChange}
                            className="form-control"
                            list="datalistOptions"
                            placeholder="What are you looking for?"
                        />

                        <select id="datalistOptions">
                            {suggestions?.map((s, index) => {
                                return (
                                    <button
                                        onClick={() => console.log(users, "ssss")}
                                        key={index}
                                        value={s.name}
                                    >
                                        {s.name}
                                    </button>
                                );
                            })}
                        </select>
                    </div>
                    <div className="form_two">
                        <button
                            type="button"
                            onClick={handleSearchButton}
                            className="btn btn-secondary"
                        >
                            Search
                        </button>
                    </div>
                </div>
            </form> */}



        </div>
    )
}

export default SearchInput