import React, { useEffect } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { getSession } from './reducers/authentication';
// import { getProfile } from 'app/shared/reducers/application-profile';
import { hasAnyAuthority } from './shared/auth/PrivateRoute';
import ErrorBoundary from './shared/error/ErrorBoundary';
import { AUTHORITIES } from './config/constants';
import AppRoutes from './route/routes';
import { useDispatch, useSelector } from 'react-redux';

// const baseHref = document.querySelector('base').getAttribute('href').replace(/\/$/, '');

export const App = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    // dispatch(getSession());
    // dispatch(getProfile());
  }, []);

  // const isAuthenticated = useSelector(state => state.authentication.isAuthenticated);
  // const isAdmin = useSelector(state => hasAnyAuthority(state.authentication.account.authorities, [AUTHORITIES.ADMIN]));
  // const ribbonEnv = useSelector(state => state.applicationProfile.ribbonEnv);
  // const isInProduction = useSelector(state => state.applicationProfile.inProduction);
  // const isOpenAPIEnabled = useSelector(state => state.applicationProfile.isOpenAPIEnabled);

  const paddingTop = '60px';
  return (
    <Router>
      <div className="app-container" style={{ paddingTop }}>
        <ErrorBoundary>
          {/*<Header
            isAuthenticated={isAuthenticated}
            isAdmin={isAdmin}
            ribbonEnv={ribbonEnv}
            isInProduction={isInProduction}
            isOpenAPIEnabled={isOpenAPIEnabled}
          />*/}
          Children
        </ErrorBoundary>
        <div className="container-fluid view-container" id="app-view-container">
          <div className="jh-card">
            <ErrorBoundary>
              <AppRoutes />
            </ErrorBoundary>
          </div>
        </div>
      </div>
    </Router>
  );
};

export default App;
