import { useReducer } from "react";

function reducer(state, action) {
  if (action.type === "increment") return state + 1;
  return state;
}

const [count, dispatch] = useReducer(reducer, 0);