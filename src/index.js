import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import getStore from './config/store';
import { Provider } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as serviceWorker from './serviceWorker';

import setupAxiosInterceptors from './config/axios-interceptor';
import { clearAuthentication } from './reducers/authentication';
import ErrorBoundary from './shared/error/ErrorBoundary';

const store = getStore();
const actions = bindActionCreators({ clearAuthentication }, store.dispatch);
setupAxiosInterceptors(() => actions.clearAuthentication('login.error.unauthorized'));

ReactDOM.render(
  <React.StrictMode>
    <ErrorBoundary>
        <Provider store={store}>
          <App />
        </Provider>
    </ErrorBoundary>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
