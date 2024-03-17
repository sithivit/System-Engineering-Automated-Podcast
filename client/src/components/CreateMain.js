import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { createTheme, ThemeProvider, styled } from '@mui/material/styles';
import Copyright from './Copyright.js';
import { Button, Collapse, Divider, Card, CardMedia, FormGroup, FormControlLabel, Checkbox, Grid } from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

import axios from 'axios';

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

const VisuallyHiddenInput = styled('input')({
    clip: 'rect(0 0 0 0)',
    clipPath: 'inset(50%)',
    height: 1,
    overflow: 'hidden',
    position: 'absolute',
    bottom: 0,
    left: 0,
    whiteSpace: 'nowrap',
    width: 1,
});

export default class CreateMain extends React.Component {

    constructor(props) {
        super(props);
        this._handleFieldChange = this._handleFieldChange.bind(this);
        this._handleSubmit = this._handleSubmit.bind(this);
    }

    state = {
        title: '',
        description: '',
        keywords: '',
        subKeywords: '',
        agentOne: '',
        agentTwo: '',
        api: '',
        isGenerated: false,
        isLocalModel: true,
        isOpenAI: false,
        isSingleAgent: true,
        isDuoAgent: false,
        responseData: '',
    }

    _handleFieldChange(e) {
        const { id, value } = e.target;
        this.setState({ [id]: value });
    }

    _handleSubmit(event) {
        event.preventDefault();

        axios.post('/api/episodes/generate/', {
            title: this.state.title,
            description: this.state.description,
            keywords: this.state.keywords,
            subKeywords: this.state.subKeywords,
            isSingleAgent: this.state.isSingleAgent,
            agentNames: [this.state.agentOne.trim(), this.state.agentTwo.trim()],
            isLocalModel: this.state.isLocalModel,
            api: this.state.api
        })
            .then((response) => {
                this.setState({ responseData: response.data, isGenerated: true });
            });


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

                            <>
                                <Divider sx={{ fontSize: "15px", mt: "50px", mb: "20px" }}>
                                    Enter Podcast Information Here
                                </Divider>

                                <TextField
                                    id="title"
                                    label="Episode Title"
                                    defaultValue=""
                                    variant="filled"
                                    required
                                    onChange={this._handleFieldChange}
                                    error={this.state.keywords.trim() === "" && this.state.isSumitAttempted}
                                    helperText={this.state.keywords.trim() === "" && this.state.isSumitAttempted ? 'Field required!' : ' '}
                                />
                                <TextField
                                    id="description"
                                    label="Episode Description"
                                    multiline
                                    rows={4}
                                    defaultValue=""
                                    variant="filled"
                                    required
                                    onChange={this._handleFieldChange}
                                    error={this.state.keywords.trim() === "" && this.state.isSumitAttempted}
                                    helperText={this.state.keywords.trim() === "" && this.state.isSumitAttempted ? 'Field required!' : ' '}
                                />
                                <TextField
                                    id="keywords"
                                    label="Topic Keywords"
                                    defaultValue=""
                                    variant="filled"
                                    required
                                    onChange={this._handleFieldChange}
                                    error={this.state.keywords.trim() === "" && this.state.isSumitAttempted}
                                    helperText={this.state.keywords.trim() === "" && this.state.isSumitAttempted ? 'Field required!' : ' '}
                                />
                                <TextField
                                    id="subKeywords"
                                    label="Subtopic Keywords"
                                    defaultValue=""
                                    variant="filled"
                                    required
                                    onChange={this._handleFieldChange}
                                    // error={this.state.keywords.trim() === "" && this.state.isSumitAttempted}
                                    helperText={this.state.keywords.trim() === "" && this.state.isSumitAttempted ? 'Field required!' : ' '}
                                />
                            </>

                            <>
                                <Divider sx={{ fontSize: "15px", my: "20px" }}>
                                    Choose number of agents
                                </Divider>

                                <Grid container alignItems={"center"}>
                                    <Grid item >
                                        <FormControlLabel
                                            control={<Checkbox />}
                                            label="Single"
                                            checked={this.state.isSingleAgent}
                                            onClick={() => this.setState({ isSingleAgent: !this.state.isSingleAgent, isDuoAgent: false })}
                                        />
                                    </Grid>
                                    <Grid item>
                                        <FormControlLabel
                                            control={<Checkbox />}
                                            label="Duo"
                                            checked={this.state.isDuoAgent}
                                            onClick={() => this.setState({ isDuoAgent: !this.state.isDuoAgent, isSingleAgent: false })}
                                        />
                                    </Grid>
                                </Grid>
                                <Collapse in={this.state.isDuoAgent}>
                                    <TextField
                                        id="agentOne"
                                        label="Agent Name 1"
                                        variant="filled"
                                        onChange={this._handleFieldChange}
                                        required={this.state.isDuoAgent}
                                        sx={{ width: "19vw" }}
                                    />
                                    <TextField
                                        id="agentTwo"
                                        label="Agent Name 2"
                                        variant="filled"
                                        onChange={this._handleFieldChange}
                                        required={this.state.isDuoAgent}
                                        sx={{ width: "19vw", ml: "2vw" }}
                                    />
                                </Collapse>
                            </>

                            <>
                                <Divider sx={{ fontSize: "15px", my: "20px" }}>
                                    Choose language model
                                </Divider>
                                <Grid container alignItems={"center"}>
                                    <Grid item >
                                        <FormControlLabel
                                            control={<Checkbox />}
                                            label="Local Model"
                                            checked={this.state.isLocalModel}
                                            onClick={() => this.setState({ isLocalModel: !this.state.isLocalModel, isOpenAI: false, api: '' })}
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
                                        id="api"
                                        label="OpenAI API"
                                        defaultValue=''
                                        variant="filled"
                                        type='password'
                                        onChange={this._handleFieldChange}
                                        required={this.state.isOpenAI}
                                        sx={{
                                            width: "40vw",
                                            maxWidth: '100%',
                                        }}
                                    />
                                </Collapse>
                            </>

                            <Grid
                                container
                                spacing={4}
                                alignItems={"center"}
                                sx={{
                                    width: "40vw",
                                    marginTop: "20px",
                                }}
                            >
                                <Grid item>
                                    <Button
                                        variant="outlined"
                                        startIcon={<CloudUploadIcon />}
                                    >
                                        Upload RAG (Optional)
                                        <VisuallyHiddenInput type="file" />
                                    </Button>
                                </Grid>
                                <Grid item>
                                    <Button
                                        variant="contained"
                                        type='submit'
                                    >
                                        Generate
                                    </Button>
                                </Grid>
                            </Grid>

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
                                image='video-path'
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