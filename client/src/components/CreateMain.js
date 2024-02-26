import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Copyright from './Copyright.js';
import { Button, Collapse, Divider, Card, CardMedia } from '@mui/material';

import axios from 'axios';

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export default class CreateMain extends React.Component {

    constructor(props) {
        super(props);
        this._handleTextFieldChange = this._handleTextFieldChange.bind(this);
        this._handleSubmit = this._handleSubmit.bind(this);
    }

    state = {
        topicKeywords: '',
        responseData: '',
        show: false,
        changed: false,
    }

    _handleTextFieldChange(e) {
        this.setState({ topicKeywords: e.target.value });
    }

    _handleSubmit(event) {
        event.preventDefault();
        this.setState({ changed: true });

        if (this.state.topicKeywords.trim() !== '') {
            axios.post('http://localhost:3001/episodes/generate/', {
                topicKeywords: this.state.topicKeywords
            })
                .then((response) => {
                    this.setState({ responseData: response.data, show: true });
                    // window.location.href = "http://localhost:3000/create-generated?topic=" + this.state.topicKeywords + "&res=" + response.data;
                });
        }


    }

    render() {
        return (

            <ThemeProvider theme={defaultTheme}>
                <CssBaseline />
                <main>
                    <form onSubmit={this._handleSubmit}>
                        <TextField
                            id="filled-multiline-static"
                            label="Topic Keywords"
                            multiline
                            rows={4}
                            defaultValue=""
                            variant="filled"
                            sx={{
                                width: "40vw",
                                maxWidth: '100%',
                                marginTop: "50px",
                                marginLeft: "30vw"
                            }}
                            onChange={this._handleTextFieldChange}
                            error={this.state.topicKeywords.trim() === "" && this.state.changed}
                            helperText={this.state.topicKeywords.trim() === "" && this.state.changed ? 'Field required!' : ' '}
                        />
                        <Button
                            variant="contained"
                            sx={{
                                width: "10vw",
                                minWidth: "100px",
                                maxWidth: "150px",
                                marginTop: "50px",
                                marginLeft: "45vw"
                            }}
                            type='submit'
                        >
                            Generate
                        </Button>
                    </form>

                    {/* The part below is displayed after form submission */}
                    <Collapse in={this.state.show}>
                        <Divider sx={{
                            width: "80vw",
                            marginTop: "50px",
                            marginLeft: "10vw",
                            fontSize: "18px"
                        }}>
                            Output
                        </Divider>
                        <Box
                            sx={{
                                width: "40vw",
                                maxWidth: '100%',
                                mx: "30vw",
                                my: '50px',
                            }}
                        >
                            {this.state.responseData}
                        </Box>
                        <Card sx={{ width: '50vw', marginLeft: '25vw' }} >
                            <CardMedia
                                component='video'
                                image='https://srvcdn2.2convert.me/dl?hash=mVdLj%2Fs0MZ%2FQax9vQl9g038gxrhZnZWSq9UCYbnxami27%2FxA0pkGhXNxe6k8tdG0VqHxrtxVMrbAsHwFtpwYH0ChQYtmTtWtkkfip9mAS%2BPgY4qsf7V47CtAVvDD6qIvBACI6FsXPZ6ng0WgnWWZL4yupaTk7wxZo391OOnx4Yu5HHvA6n%2FgnUVfjuYOjFljdVpQMyzn3wgEmH%2BpJyBmk1pnMjSqpciZiT3%2FKcIQnO8w8UAjqyQfLevPyhEZanqOh3m6zdCGyYqlq0YoUjAmtCcJNXXFqedwAApUcqub1zM%3D'
                                controls
                            />
                        </Card>
                        <Button
                            variant="contained"
                            sx={{
                                width: "10vw",
                                minWidth: "100px",
                                maxWidth: "150px",
                                marginTop: "50px",
                                marginLeft: "45vw"
                            }}
                        >
                            Upload
                        </Button>
                    </Collapse>
                </main>
                {/* Footer */}
                <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
                    <Copyright />
                </Box>
                {/* End footer */}
            </ThemeProvider >
        );
    }
}