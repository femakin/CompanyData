import React, { useEffect, useState } from "react";
import config from "../config";
import "../styles/Category.css";
import { Link } from "react-router-dom";
import SearchInput from "./SearchInput";

function Category() {
  let [categories, setCategories] = useState([]);
  const data = [
    {
      name: "Sport",
      count: 200,
    },
    {
      name: "Social",
      count: 50,
    },
    {
      name: "Web",
      count: 500,
    },
    {
      name: "Agriculture",
      count: 1000,
    },
    {
      name: "Sport",
      count: 200,
    },
    {
      name: "Social",
      count: 50,
    },
    {
      name: "Web",
      count: 500,
    },
    {
      name: "Agriculture",
      count: 1000,
    },
    {
      name: "Sport",
      count: 200,
    },
    {
      name: "Social",
      count: 50,
    },
    {
      name: "Web",
      count: 500,
    },
    {
      name: "Agriculture",
      count: 1000,
    },
    {
      name: "Sport",
      count: 200,
    },
    {
      name: "Social",
      count: 50,
    },
    {
      name: "Web",
      count: 500,
    },
    {
      name: "Agriculture",
      count: 1000,
    },
  ];


  useEffect(() => {
    const getCategories = async () => {
      let categories = await fetch(`${config.BASE_URL}/socialgroup`).then(r => r.json());
      setCategories(categories);
      // console.log(categories, 'categoriesss')
    }

    getCategories();
  }, []);





  return (
    <div>
      {/* <SearchInput /> */}
      <section className="">
        <div className="category_home ">
          {categories.map((x, i) => {
            return (
              <div className=" category_content">
                <Link className="categ-link" to={`/category/${x._id}`}>  {x._id} {x.count}</Link>

              </div>
            );
          })}

          {/* <div className="flex flex-wrap w-1/3">
        <div className="w-full p-1 md:p-2">
          <img alt="gallery" className="block object-cover object-center w-full h-full rounded-lg"
            src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/Nature/4-col/img%20(73).webp"/>
        </div>
      </div>
      <div className="flex flex-wrap w-1/3">
        <div className="w-full p-1 md:p-2">
          <img alt="gallery" className="block object-cover object-center w-full h-full rounded-lg"
            src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/Nature/4-col/img%20(74).webp"/>
        </div>
      </div>
      <div className="flex flex-wrap w-1/3">
        <div className="w-full p-1 md:p-2">
          <img alt="gallery" className="block object-cover object-center w-full h-full rounded-lg"
            src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/Nature/4-col/img%20(75).webp"/>
        </div>
      </div>
      <div className="flex flex-wrap w-1/3">
        <div className="w-full p-1 md:p-2">
          <img alt="gallery" className="block object-cover object-center w-full h-full rounded-lg"
            src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/Nature/4-col/img%20(70).webp"/>
        </div>
      </div>
      <div className="flex flex-wrap w-1/3">
        <div className="w-full p-1 md:p-2">
          <img alt="gallery" className="block object-cover object-center w-full h-full rounded-lg"
            src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/Nature/4-col/img%20(76).webp"/>
        </div>
      </div>
      <div className="flex flex-wrap w-1/3">
        <div className="w-full p-1 md:p-2">
          <img alt="gallery" className="block object-cover object-center w-full h-full rounded-lg"
            src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/Nature/4-col/img%20(72).webp"/>
        </div>
      </div> */}
        </div>
      </section>
    </div>
  );
}

export default Category;
