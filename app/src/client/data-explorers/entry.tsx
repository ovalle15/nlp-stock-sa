import React from 'react';
import { createRoot } from 'react-dom/client';
import { ChakraProvider, ColorModeScript, extendTheme } from '@chakra-ui/react';

import type { InitialArticleDataBySlugPageData } from '@nlpssa-app-types/common/main';
import { ArticleDataApp } from 'client/data-explorers/article-data/components';
import AppStateProvider from 'client/data-explorers/store/AppStateProvider';
// import reportWebVitals from 'client/reportWebVitals';

// type ArticlePageData = InitialArticleDataBySlugPageData & {
//     stockSlug: string;
// };

window.renderApp = async (initialPageData) => {
    const root = createRoot(document.getElementById('nlpssa-main'));
    console.log({ page: 'article-data', initialPageData });

    const theme = extendTheme({
        initialColorMode: 'system',
        useSystemColorMode: true,
    });

    const stockSlug =
        (initialPageData.stockSlug as string) || window.location.pathname.replace(/^\/\S+\/(?=[^\/]+$)/gim, '');

    root.render(
        <AppStateProvider>
            <ChakraProvider theme={theme}>
                <ColorModeScript initialColorMode={theme.config.initialColorMode} />
                <ArticleDataApp
                    initialPageData={initialPageData as InitialArticleDataBySlugPageData}
                    stockSlug={stockSlug}
                />
            </ChakraProvider>
        </AppStateProvider>,
    );
};

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
