import React, { Component } from 'react';
import { connect } from 'react-redux';

import { authSignUp } from '../../store/actions/authAction';


class SignUpForm extends Component {
  constructor(props) {
    super(props)
    this.state = {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      errors: {}
    }
  }

  handleChange = e => {
    this.setState({
      [e.target.id]: e.target.value
    })
  }

  handleSubmit = e => {
    e.preventDefault()
    var { first_name, last_name, email, password } = this.state;
    var user = {
      first_name,
      last_name,
      email,
      password,
    }
    this.props.signUp(user)
  }

  render() {
    const { error } = this.state
    return (
      <div className="signupForm">
        <from>
          <h5>Sign Up</h5>
          <div>
            <label htmlFor="email">Email</label>
            <input type="text" id="email" onChange={} />
          </div>
          <div>
            <label htmlFor="password">Password</label>
            <input type="password" id="password" onChange={} />
          </div>
          <button>Signup</button>

          <div className="errors">
            { error.first_name ? <p>first_name: error</p> : null }
            { error.last_name ? <p>last_name: error</p> : null }
            { error.email ? <p>email: error</p> : null }
            { error.password ? <p>password: error</p> : null }
          </div>
        </from>
      </div>
    )

  }
}

const mapDispatchToProps = dispatch => {
  return {
    signUp: newUser => dispatch(authSignUp(newUser))
  }
}

export default connect(null, mapDispatchToProps)(SignUpForm)