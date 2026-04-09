import { createContext, useContext } from "react";

const MyContext = createContext();

const value = useContext(MyContext);