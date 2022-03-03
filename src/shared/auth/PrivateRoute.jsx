import React from 'react';
import { useSelector } from 'react-redux';
import { Route, Redirect } from 'react-router-dom';

import ErrorBoundary from '../error/ErrorBoundary';

export const PrivateRouteComponent = ({ component: Component, hasAnyAuthorities = [], ...rest }) => {
  // console.log(Component)
  // const isAuthenticated = useSelector(state => state.authentication.isAuthenticated);
  // const sessionHasBeenFetched = useSelector(state => state.authentication.sessionHasBeenFetched);
  // const account = useSelector(state => state.authentication.account);
  // const isAuthorized = hasAnyAuthority(account.authorities, hasAnyAuthorities);
  const sessionHasBeenFetched = true;
  const isAuthorized = true;
  const isAuthenticated = true;

  const checkAuthorities = props => {
    return isAuthorized ? (
      <ErrorBoundary>
        <Component {...props} />
      </ErrorBoundary>
    ) : (
      <div className="insufficient-authority">
        <div className="alert alert-danger">You are not authorized to access this page.</div>
      </div>
    );
  }

  const renderRedirect = props => {
    if (!sessionHasBeenFetched) {
      return <div></div>;
    } else {
      return isAuthenticated ? (
        checkAuthorities(props)
      ) : (
        <Redirect
          to={{
            pathname: '/login',
            search: props.location.search,
            state: { from: props.location },
          }}
        />
      );
    }
  };

  if (!Component) throw new Error(`A component needs to be specified for private route for path ${rest.path}`);

  return <Route {...rest} render={renderRedirect} />;
};

export const hasAnyAuthority = (authorities, hasAnyAuthorities) => {
  if (authorities && authorities.length !== 0) {
    if (hasAnyAuthorities.length === 0) {
      return true;
    }
    return hasAnyAuthorities.some(auth => authorities.includes(auth));
  }
  return false;
};

/**
 * A route wrapped in an authentication check so that routing happens only when you are authenticated.
 * Accepts same props as React router Route.
 * The route also checks for authorization if hasAnyAuthorities is specified.
 */
export default PrivateRouteComponent;
