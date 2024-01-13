<script>
    import axios from 'axios';
    import { page } from '$app/stores';

    let isLoading = true;
    let error = null;
    let data;
    
    $: truncatedTitle = $page.params.title;
    $: if (truncatedTitle) fetchData(truncatedTitle);
    
    async function fetchData() {
        try {
            const url = "http://localhost:8000/article/" + truncatedTitle;
            console.log("calling ", url);
            const response = await axios.get(url);
            data = response.data;
        } catch (e) {
            error = e;
        } finally {
            isLoading = false;
        }
    }

</script>

{#if isLoading }
    <p>Loading Article...</p>
{:else if error}
    <p>Failed to fetch: {error.message}</p>
{:else}
    <h1>{data.title}</h1>
    <p>{data.content}</p>
{/if}

<a href="/">Back to Home</a>