import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Copyright from './Copyright.js';
import { Button, Collapse, Divider, Card, CardMedia, FormGroup, FormControlLabel, Checkbox, Grid } from '@mui/material';

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
        isGenerated: false,
        isSumitAttempted: false,
        isLocalModel: true,
        isOpenAI: false,
        isSingle: true,
        isMultiple: false,
    }

    _handleTextFieldChange(e) {
        this.setState({ topicKeywords: e.target.value });
    }

    _handleSubmit(event) {
        event.preventDefault();
        this.setState({ isSumitAttempted: true });

        if (this.state.topicKeywords.trim() !== '') {
            axios.post('http://localhost:3001/episodes/generate/', {
                topicKeywords: this.state.topicKeywords
            })
                .then((response) => {
                    this.setState({ responseData: response.data, isGenerated: true });
                });
        }


    }

    _handleCheckbox(e) {
        this.setState({ isOpenAI: e });
    }

    render() {
        return (

            <ThemeProvider theme={defaultTheme}>
                <CssBaseline />
                <main>
                    <form onSubmit={this._handleSubmit}>
                        <FormGroup
                            sx={{
                                width: "40vw",
                                maxWidth: '100%',
                                marginLeft: "30vw",
                            }}
                        >
                            <Divider sx={{ fontSize: "15px", mt: "50px", mb: "20px" }}>
                                Enter Topic Keywords Here
                            </Divider>
                            <TextField
                                id="filled-multiline-static"
                                label="Topic Keywords"
                                multiline
                                rows={4}
                                defaultValue=""
                                variant="filled"
                                onChange={this._handleTextFieldChange}
                                error={this.state.topicKeywords.trim() === "" && this.state.isSumitAttempted}
                                helperText={this.state.topicKeywords.trim() === "" && this.state.isSumitAttempted ? 'Field required!' : ' '}
                            />
                            <Divider sx={{ fontSize: "15px", my: "20px" }}>
                                Choose number of guests
                            </Divider>
                            <Grid container alignItems={"center"}>
                                <Grid item >
                                    <FormControlLabel
                                        control={<Checkbox />}
                                        label="Single"
                                        checked={this.state.isSingle}
                                        onClick={() => this.setState({ isSingle: !this.state.isSingle, isMultiple: false })}
                                    />
                                </Grid>
                                <Grid item>
                                    <FormControlLabel
                                        control={<Checkbox />}
                                        label="Multiple"
                                        checked={this.state.isMultiple}
                                        onClick={() => this.setState({ isMultiple: !this.state.isMultiple, isSingle: false })}
                                    />
                                </Grid>
                            </Grid>
                            <Divider sx={{ fontSize: "15px", my: "20px" }}>
                                Choose language model
                            </Divider>
                            <Grid container alignItems={"center"}>
                                <Grid item >
                                    <FormControlLabel
                                        control={<Checkbox />}
                                        label="Local Model"
                                        checked={this.state.isLocalModel}
                                        onClick={() => this.setState({ isLocalModel: !this.state.isLocalModel, isOpenAI: false })}
                                    />
                                </Grid>
                                <Grid item>
                                    <FormControlLabel
                                        control={<Checkbox />}
                                        label="OpenAI"
                                        checked={this.state.isOpenAI}
                                        onClick={() => this.setState({ isOpenAI: !this.state.isOpenAI, isLocalModel: false })}
                                    />
                                </Grid>
                            </Grid>
                            <Collapse in={this.state.isOpenAI}>
                                <TextField
                                    label="OpenAI API"
                                    defaultValue=''
                                    variant="filled"
                                    type='password'
                                    sx={{
                                        width: "40vw",
                                        maxWidth: '100%',
                                    }}
                                />
                            </Collapse>
                            <Button
                                variant="contained"
                                sx={{
                                    width: "10vw",
                                    minWidth: "100px",
                                    maxWidth: "150px",
                                    marginTop: "50px",
                                    marginLeft: "15vw"
                                }}
                                type='submit'
                            >
                                Generate
                            </Button>

                        </FormGroup>
                    </form>

                    {/* The part below is displayed after form submission */}
                    <Collapse in={this.state.isGenerated}>
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
                                image='https://srvcdn15.2convert.me/dl?hash=S61wRx5oRhsl49MKlNzq7ku7eIICJB6seE6VUht9sLO91USCeLpculJ4Mx8AJwtAbpATVwPSRCI0QmC0ElSHjSuknVLHmKMO1RLYG8qvik1aplw3lekeJO29J9wRgehtlv%2Bmckz%2B8J6Xn%2BOv4g4CxIbh3HAcWyPzy%2FAkbDsyXgsJufMRfOhxA2yaZvapu85oeEKfeD%2BaMrsdDl4BiQHlWRn8q7DbYvlxhMfWtyZmgQ5y3eIPFan7HIPsmcGByMrZJIsab01EEGG7xvJzxMUNYJTkaDoSab%2FPgSNclAJ2jsA%3D'
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