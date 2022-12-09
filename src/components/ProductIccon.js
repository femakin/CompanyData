import React, { useState } from 'react'
import { Link } from 'react-router-dom';
import '../styles/ProductIcon.css'
import { useNavigate } from "react-router-dom";
import SearchInput from './SearchInput';


function ProductIccon({ item }) {
    const [showMore, setShowMore] = useState(false);
    const navigate = useNavigate();
    return (


        <>
            {/* <div className="searchcontainer">
                <SearchInput />
            </div> */}

            <div>

                {
                    item.map((x, i) => {
                        return (
                            <section>
                                <div classNameName='product_container' >
                                    <div className="flex flex-row ">
                                        <div className="block p-6 rounded-lg shadow-lg bg-white max-w-sm">
                                            <h5 className="text-gray-900 text-xl leading-tight font-medium mb-2">Name: {x.name}</h5>
                                            <p className="text-gray-700 text-base mb-4">number of employees &nbsp; {x?.number_of_employees === null ? 'NA' : x?.number_of_employees}</p>
                                            <p className="text-gray-700 text-base mb-4">Founded Year &nbsp; {x?.founded_year === null ? 'NA' : x?.founded_year}</p>
                                            <button onClick={() => window.open(`${x?.homepage_url}`, '_blank')} type="button" className=" inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Homepage</button>
                                        </div>
                                    </div>
                                </div>



                            </section>
                        )
                    })
                }

            </div>
        </>





    )
}

export default ProductIccon