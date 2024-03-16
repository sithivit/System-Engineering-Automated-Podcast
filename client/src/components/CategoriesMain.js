import * as React from 'react';
import { Button, Card, CardActions, CardContent, CardMedia, CssBaseline, Grid, Box, Typography, Container, TextField, Divider } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Copyright from './Copyright.js'

import axios from 'axios';

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export default class CategoriesMain extends React.Component {
    state = {
        episodes: []
    }

    componentDidMount() {
        axios.get(`/episodes`)
            .then(res => {
                const episodes = res.data;
                this.setState({ episodes });
            })
    }

    render() {
        return (

            <ThemeProvider theme={defaultTheme}>
                <CssBaseline />
                <main>
                    <Box
                        sx={{
                            width: "60vw",
                            maxWidth: '100%',
                            marginTop: "50px",
                            marginLeft: "20vw"
                        }}
                    >
                        <TextField fullWidth label="Search episodes..." id="search" />
                    </Box>
                    <Divider sx={{
                        width: "80vw",
                        marginTop: "50px",
                        marginLeft: "10vw",
                        fontSize: "18px",
                        fontWeight: "bold"
                    }}>
                        Categories
                    </Divider>
                    <Container sx={{ py: 8 }} maxWidth="md">
                        <Grid container spacing={4}>
                            {this.state.episodes.map((episode) => (
                                <Grid item key={episode} xs={12} sm={6} md={4}>
                                    <Card
                                        sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}
                                    >
                                        <CardMedia
                                            component="div"
                                            sx={{
                                                // 16:9
                                                pt: '56.25%',
                                            }}
                                            image="https://source.unsplash.com/random?wallpapers"
                                        />
                                        <CardContent sx={{ flexGrow: 1 }}>
                                            <Typography gutterBottom variant="h5" component="h2">
                                                {episode.title}
                                            </Typography>
                                            <Typography>
                                                {episode.description}
                                            </Typography>
                                        </CardContent>
                                        <CardActions>
                                            <Button size="small">View</Button>
                                            <Button size="small">Edit</Button>
                                        </CardActions>
                                    </Card>
                                </Grid>
                            ))}
                        </Grid>
                    </Container>
                </main>
                {/* Footer */}
                <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
                    <Copyright />
                </Box>
                {/* End footer */}
            </ThemeProvider>
        );
    }
}