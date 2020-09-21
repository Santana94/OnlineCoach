import React from 'react';

class CreateUser extends React.Component {
    constructor (){
        super();
        
        this.state = {
            gender: 1
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        var postData = {
            username: this.state.username,
            password: this.state.password,
            gender: this.state.gender,
            age: this.state.age,
            height: this.state.height,
        }
        console.log(postData);
        var requestOptions = {
            method: 'POST',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(postData)
        };
          
        fetch("http://localhost:8000/user_profile/", requestOptions)
            .then(response => response.text())
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    render (){
        return (
            <form onSubmit={this.handleSubmit} className="ui form" method="post">
                <h4 className="ui dividing header">Cadastro de Usuário</h4>
                <div className="field">
                    <label>
                        Username:
                        <input type="text" name="username" placeholder="Username" onChange={this.handleChange}/>
                    </label>
                </div>
                <div className="field">
                    <label>
                        Senha:
                        <input type="password" name="password" placeholder="Senha" onChange={this.handleChange} />
                    </label>
                </div>
                <div className="three fields">
                    <div className="field">
                        <label>
                            Idade:
                            <input type="number" name="age" placeholder="Idade" onChange={this.handleChange} />
                        </label>
                    </div>
                    <div className="field">
                        <label>Gênero</label>
                        <select className="ui fluid dropdown" name="gender" onChange={this.handleChange}>
                            <option value="1">Feminino</option>
                            <option value="0">Masculino</option>
                        </select>
                    </div>
                    <div className="field">
                        <label>
                            Altura:
                            <input type="number" name="height" placeholder="Altura" onChange={this.handleChange} />
                        </label>
                    </div>
                </div>
                <button className="ui button">Criar</button>
            </form>
        );
    }
}

export default CreateUser;