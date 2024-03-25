import * as React from 'react';
import { CssBaseline, Box, Typography, Container, Divider } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Copyright from './Copyright.js'

// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export default function IndexMain() {
    return (
        <ThemeProvider theme={defaultTheme}>
            <CssBaseline />
            <main>
                <Box sx={{
                    bgcolor: 'background.paper',
                    pt: 15,
                    pb: 6,
                }}>
                    <Container sx={{ py: 8 }} maxWidth="sm">
                        <Typography
                            component="h1"
                            variant="h2"
                            align="center"
                            color="text.primary"
                            gutterBottom
                        >
                            AI Podcast
                        </Typography>
                        <Typography
                            component="h1"
                            variant="h4"
                            align="center"
                            color="text.secondary"
                            gutterBottom
                        >
                            "enhance your experience"
                        </Typography>
                    </Container>
                    <Divider sx={{
                        width: "40vw",
                        marginLeft: "30vw",
                    }} />
                    <Container sx={{ py: 8 }} maxWidth="md">
                        <Typography variant="h5" align="center" color="text.primary" paragraph>
                            Welcome to our AI Podcast app! Explore the world of artificial intelligence with engaging conversations and insights. From industry experts to enthusiasts, discover the latest trends and innovations shaping AI. Join us on this journey of discovery and inspiration!
                        </Typography>
                    </Container>
                </Box>
                <Box>
                    <Container sx={{ pt: 8, pb: 8, px: 3, backgroundColor: 'grey.100', border: '1px solid grey.300', borderRadius: '5px' }} maxWidth="md">
                        <Typography variant="body2" align="justify" color="text.secondary" paragraph style={{ fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif' }}>
                            DISCLAIMER: This podcast features computer-generated voices emulating the likeness of real individuals, and the content is entirely produced using AI language models. The voices, opinions, and conversations presented in this podcast are entirely fictional and do not represent the thoughts, beliefs, or attitudes of the individuals whose personas are replicated. The content is created for entertainment purposes only and is not intended to convey the genuine perspectives of any actual person. The use of AI technology in this context is an exploration of the capabilities of language models and should not be mistaken for authentic dialogue. Any similarities to real events, individuals, or entities are coincidental. Viewers are advised to interpret this content as a creative exercise and not as an accurate portrayal of the beliefs or opinions of the individuals depicted or any associated organizations.
                        </Typography>
                    </Container>
                </Box>

            </main>
            <footer>
                <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
                    <Copyright />
                </Box>
            </footer>
        </ThemeProvider>
    );
}