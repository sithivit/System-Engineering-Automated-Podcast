import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Divider } from '@mui/material';

function Copyright() {
    return (
        <Typography variant="body2" color="text.secondary" align="center">
            {'Copyright © '}
            <Link color="inherit" href="https://mui.com/">
                Your Website
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

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
            </main>
            <footer>
                <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
                    <Copyright />
                </Box>
            </footer>
        </ThemeProvider>
    );
}