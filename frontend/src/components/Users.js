import React from 'react';
import CreateUser from './CreateUser';

class Users extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        error: null,
        isLoaded: false,
        users: []
      };
    }
  
    componentDidMount() {
      var headers = new Headers();
      headers.append("Token", "07293a2a4b23cfc6b3831551878e5b111075e7ec");
      headers.append('Access-Control-Allow-Origin', 'http://localhost:3000');
      headers.append('Access-Control-Allow-Credentials', 'true');

      var requestOptions = {
        method: 'GET',
        headers: headers,
        redirect: 'follow'
      };
      fetch("http://localhost:8000/user_profile/", requestOptions)
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              users: result.results
            });
          },
          // Note: it's important to handle errors here
          // instead of a catch() block so that we don't swallow
          // exceptions from actual bugs in components.
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }
  
    render() {
      const { error, isLoaded, users } = this.state;
      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading...</div>;
      } else if (users.length) {
        return (
          <ul>
            {users.map(user => (
              <li key={user.name}>
                {user.id} {user.name}
              </li>
            ))}
          </ul>
        );
      } else {
        return <CreateUser />
      }
    }
  }

export default Users;