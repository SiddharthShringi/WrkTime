import React, { Component } from 'react';

import SignUpForm from './SignUpForm';
import LoginForm from './LoginForm';


class AuthWrapper extends Component {
  constructor(props) {
    super(props)
    this.state = {
      isLogin: true,
      isSignup: false
    }
  }

  handlClick = e => {
    if (e.target.id === 'login') {
      this.setState({
        isLogin: true,
        isSignup: false
      })
    }
    if (e.target.id === 'signup') {
      this.setState({
        isLogin: false,
        isSignup: true
      })
    }
  }

  render() {
    const { isLogin, isSignup } = this.state
    let authForm;
    if (isLogin) {
      authForm = <LoginForm />
    }
    if (isSignup) {
      authForm = <SignUpForm />
    }
    return (
      <div className="auth-wrapper">
        <div className="form-option">
          <p id="signup" onClick={this.handlClick}>SignUp</p>
          <p id="login" onClick={this.handlClick}>Login</p>
        </div>
        <div className="form">
          { authForm }
        </div>
      </div>
    )
  }
}

export default AuthWrapper;