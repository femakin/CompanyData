import Navbar from "./Navbar";
import Search from "./Search";
// import Search from "./Search";

export default function Header() {
    let linkStyle = { color: "#00684a" };
    let activeLinkStyle = { backgroundColor: "#00684a" };

    return (
        <div className="header">
            <Navbar />

            {/* <Search /> */}


        </div>
    )
}