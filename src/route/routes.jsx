import React from 'react';
import { Switch } from 'react-router-dom';
import Home from '../pages/Home';
import PrivateRoute from '../shared/auth/PrivateRoute';
import ErrorBoundary from '../shared/error/ErrorBoundary';
import ErrorBoundaryRoute from '../shared/error/ErrorBoundaryRoute';
import PageNotFound from '../shared/error/PageNotFound';
import { AUTHORITIES } from '../config/constants';
//
const Routes = () => {
  return (
    <div className="view-routes">
      <Switch>
        {/*<ErrorBoundaryRoute path="/logout" component={Logout} />
        <ErrorBoundaryRoute path="/account/register" component={Register} />
        <ErrorBoundaryRoute path="/account/activate/:key?" component={Activate} />
        <ErrorBoundaryRoute path="/account/reset/request" component={PasswordResetInit} />
        <ErrorBoundaryRoute path="/account/reset/finish/:key?" component={PasswordResetFinish} />
        <PrivateRoute path="/admin" component={Admin} hasAnyAuthorities={[AUTHORITIES.ADMIN]} />
        <PrivateRoute path="/account" component={Account} hasAnyAuthorities={[AUTHORITIES.ADMIN, AUTHORITIES.USER]} />
        <ErrorBoundaryRoute path="/" exact component={Home} /> 
        <PrivateRoute path="/" component={Home} hasAnyAuthorities={[AUTHORITIES.USER]} />*/}
        <PrivateRoute path="/" component={Home} hasAnyAuthorities={[AUTHORITIES.USER]} />
        <ErrorBoundaryRoute component={PageNotFound} />
      </Switch>
    </div>
  );
};

export default Routes;
