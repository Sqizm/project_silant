import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../slice/authSlice';
import userReducer from '../../main/authMain/user_data/userDataSlice';

const store = configureStore({
    reducer: {
        auth: authReducer,
        userData: userReducer,
    }
});

export default store;