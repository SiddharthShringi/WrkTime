import React, { Component } from 'react';
import { connect } from 'react-redux';

import { authSignUp } from '../../store/actions/authAction';


class SignUpForm extends Component {
  constructor(props) {
    super(props)
    this.state = {
      firstName: '',
      lastName: '',
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
    var { firstName, lastName, email, password } = this.state;
    var user = {
      firstName,
      lastName,
      email,
      password,
    }
    this.props.signUp(user)
  }

  render() {
    const { error } = this.state
    return (
      <div className="signupForm">
        <form onSubmit={this.handleSubmit}>
          <h5>Sign Up</h5>
          <div>
            <label htmlFor="firstName">First Name</label>
            <input type="text" id="firstName" onChange={this.handleChange} />
          </div>
          <div>
            <label htmlFor="lastName">Last Name</label>
            <input type="text" id="lastName" onChange={this.handleChange} />
          </div>
          <div>
            <label htmlFor="email">Email</label>
            <input type="text" id="email" onChange={this.handleChange} />
          </div>
          <div>
            <label htmlFor="password">Password</label>
            <input type="password" id="password" onChange={this.handleChange} />
          </div>
          <button>Signup</button>

          {/* <div className="errors">
            { error.firstName ? <p>first_name: error</p> : null }
            { error.lastName ? <p>last_name: error</p> : null }
            { error.email ? <p>email: error</p> : null }
            { error.password ? <p>password: error</p> : null }
          </div> */}
        </form>
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