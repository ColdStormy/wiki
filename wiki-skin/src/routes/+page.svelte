<script>
    import axios from 'axios';
    
    async function fetchData() {
        try {
            const response = await axios.get('http://localhost:8000/');
            return response.data;
        } catch (error) {
            throw new Error(`HTTP error! status: ${error}`);
        }
    }


    const dataPromise = fetchData();
</script>

{#await dataPromise}
    <p>Loading...</p>
{:then data}
    <h1>{data.Hello}</h1>
{:catch error}
    <p>Failed to fetch: {error.message}</p>
{/await}

<a href="/article/Some_weirdo_title">Some weirdo title</a>