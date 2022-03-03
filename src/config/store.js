import { configureStore } from '@reduxjs/toolkit';
import reducer from '../reducers';


const store = configureStore({
  reducer,
  }
)

const getStore = () => store;
export default getStore;
