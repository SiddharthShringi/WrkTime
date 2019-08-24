import React, { Component } from 'react';
import { connect } from 'react-redux';
import { authLogin } from '../../store/actions/authAction';



class LoginForm extends Component {
  constructor(props) {
    super(props)
    this.state = {
      email: '',
      password: '',
      error: ''
    }
  }

  handleChange = e => {
    this.setState({
      [e.target.id]: e.target.value
    })
  }

  handleSubmit = e => {
    e.preventDefault()
    var { email, password } = this.state;
    var user = {
      email,
      password
    }
    this.props.logIn(user)
  }

  render() {
    const { error } = this.state
    return (
      <div className="loginForm">
        <form onSubmit={this.handleSubmit}>
          <h5>Login</h5>
          <div>
            <label htmlFor="email">Email</label>
            <input type="text" id="email" onChange={this.handleChange} />
          </div> 
          <div>
            <label htmlFor="password">Password</label>
            <input type="text" id="password" onChange={this.handleChange} />
          </div>
          <button>Login</button>
        </form>
      </div>
    )
  }
}


const mapDispatchToProps = dispatch => {
  return {
    logIn: user => dispatch(authLogin(user))
  }
}

export default connect(null, mapDispatchToProps)(LoginForm)