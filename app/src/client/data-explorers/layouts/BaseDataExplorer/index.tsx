import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import type { AbstractPageData } from '@nlpssa-app-types/common/main';
import { BasePage, ErrorElement } from 'client/common/layouts';
import {
    ArticleDataBySlugExplorer,
    ArticleDataExplorer,
} from 'client/data-explorers/explorers/article-data/components';
import { DataExplorerView } from 'client/data-explorers/layouts';
import AppStateProvider from 'client/data-explorers/store/AppStateProvider';

function BaseDataExplorer({ initialPageData }: { initialPageData: AbstractPageData }) {
    const browserRouter = createBrowserRouter([
        {
            path: '/app/data-explorers',
            element: <DataExplorerView />,
            errorElement: <ErrorElement />,
            children: [
                {
                    path: 'article-data/:stockSlug',
                    element: <ArticleDataBySlugExplorer />,
                },
                {
                    path: 'article-data',
                    element: <ArticleDataExplorer />,
                },
                // {
                //     path: 'stocks/:stockSlug',
                //     element: <ArticleDataBySlugExplorer />,
                // },
                // {
                //     path: 'stocks',
                //     element: <ArticleDataExplorer />,
                // },
            ],
        },
    ]);

    console.log('data-explorers - BaseDataExplorer', { initialPageData });
    return (
        <BasePage>
            <AppStateProvider initialState={initialPageData}>
                <RouterProvider router={browserRouter} />
            </AppStateProvider>
        </BasePage>
    );
}

export default BaseDataExplorer;
