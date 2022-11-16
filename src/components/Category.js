import React from "react";
import "../styles/Category.css";

function Category() {
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

  return (
    <div>
      <section className="">
        <div className="category_home ">
          {data.map((x, i) => {
            return (
              <div className=" category_content">
                <h1>
                  {x.name} {x.count}
                </h1>
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
