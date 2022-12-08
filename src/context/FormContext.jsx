import { createContext, useState } from 'react'

export const AllContext = createContext();

export const UserProvider = ({ children }) => {



    const [users, setUsers] = useState('')

    return (
        <AllContext.Provider
            value={{
                users, setUsers
            }}
        >
            {children}
        </AllContext.Provider>
    );
}