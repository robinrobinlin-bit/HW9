document.addEventListener("DOMContentLoaded", () => {
    const chatInput = document.getElementById("chat-input");
    const sendBtn = document.getElementById("send-btn");
    const chatMessages = document.getElementById("chat-messages");
    const resultsGrid = document.getElementById("results-grid");
    const placeholderState = document.getElementById("placeholder-state");
    const resultsCount = document.getElementById("results-count");
    const chipBtns = document.querySelectorAll(".chip-btn");

    // Send chat request
    async function sendQuery(message) {
        if (!message || message.trim() === "") return;

        // 1. Add User Message
        appendMessage(message, "user");
        chatInput.value = "";
        chatInput.focus();

        // 2. Add Typing Indicator
        const typingId = appendTypingIndicator();
        scrollChatToBottom();

        try {
            // 3. API Call
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error("Network response error");
            }

            const data = await response.json();

            // 4. Remove Typing Indicator & Add System Response
            removeMessageById(typingId);
            appendMessage(data.reply, "system");
            
            // 5. Update Results Grid
            updateResults(data.results);
            scrollChatToBottom();

        } catch (error) {
            removeMessageById(typingId);
            appendMessage("Sorry, I encountered an error communicating with the server. Please try again.", "system");
            scrollChatToBottom();
            console.error("Error sending query:", error);
        }
    }

    // Helper: Append chat message bubble
    function appendMessage(text, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        
        // Handle basic markdown formatting (e.g. bolding **text**)
        const formattedText = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                                  .replace(/\n/g, '<br>');

        messageDiv.innerHTML = `
            <div class="message-content">
                <p>${formattedText}</p>
            </div>
        `;
        chatMessages.appendChild(messageDiv);
        scrollChatToBottom();
    }

    // Helper: Add typing loading bubble
    function appendTypingIndicator() {
        const id = "typing-" + Date.now();
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", "system");
        messageDiv.id = id;
        messageDiv.innerHTML = `
            <div class="message-content" style="display: flex; gap: 4px; padding: 12px 20px;">
                <span class="typing-dot" style="width: 6px; height: 6px; border-radius: 50%; background: #8e8fa1; animation: typingBounce 1s infinite 0.1s;"></span>
                <span class="typing-dot" style="width: 6px; height: 6px; border-radius: 50%; background: #8e8fa1; animation: typingBounce 1s infinite 0.2s;"></span>
                <span class="typing-dot" style="width: 6px; height: 6px; border-radius: 50%; background: #8e8fa1; animation: typingBounce 1s infinite 0.3s;"></span>
            </div>
        `;
        chatMessages.appendChild(messageDiv);
        
        // Inline typing animation styles
        if (!document.getElementById("typing-animation-style")) {
            const style = document.createElement("style");
            style.id = "typing-animation-style";
            style.innerHTML = `
                @keyframes typingBounce {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(-4px); }
                }
            `;
            document.head.appendChild(style);
        }
        
        return id;
    }

    function removeMessageById(id) {
        const element = document.getElementById(id);
        if (element) {
            element.remove();
        }
    }

    function scrollChatToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Update movie search result list
    function updateResults(movies) {
        resultsGrid.innerHTML = "";
        
        if (!movies || movies.length === 0) {
            resultsCount.textContent = "0 movies found";
            resultsGrid.appendChild(placeholderState);
            placeholderState.style.display = "flex";
            placeholderState.querySelector("h3").textContent = "No Movies Found";
            placeholderState.querySelector("p").textContent = "Try asking for different keywords, categories, or rankings.";
            return;
        }

        // Hide placeholder state
        placeholderState.style.display = "none";
        resultsCount.textContent = `${movies.length} movies found`;

        // Render movie cards
        movies.forEach((movie, index) => {
            const card = document.createElement("div");
            card.classList.add("movie-card");
            
            // Build categories list HTML
            const categoriesHtml = movie.categories.map(cat => `<span class="movie-cat">${cat}</span>`).join("");
            const regionsText = movie.regions.join(", ") || "N/A";
            const scoreText = movie.score ? movie.score.toFixed(1) : "N/A";

            card.innerHTML = `
                <div class="rank-badge">${index + 1}</div>
                <div class="movie-cover-wrapper">
                    <img class="movie-cover" src="${movie.cover_url}" alt="${movie.title}" onerror="this.src='https://images.unsplash.com/photo-1542204172-e7052809f852?auto=format&fit=crop&w=150&q=80'">
                </div>
                <div class="movie-details">
                    <div class="movie-top">
                        <h3 class="movie-title" title="${movie.title}">${movie.title}</h3>
                        <span class="movie-score">
                            <i class="fa-solid fa-star"></i> ${scoreText}
                        </span>
                    </div>
                    <div class="movie-mid">
                        ${categoriesHtml}
                    </div>
                    <div class="movie-bottom">
                        <div class="movie-meta">
                            <span><i class="fa-solid fa-globe"></i> ${regionsText}</span>
                            <span><i class="fa-solid fa-clock"></i> ${movie.duration}</span>
                        </div>
                        <a href="${movie.detail_link}" target="_blank" class="detail-btn">
                            Detail <i class="fa-solid fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            `;
            resultsGrid.appendChild(card);
        });
    }

    // Event listeners for inputs
    sendBtn.addEventListener("click", () => {
        sendQuery(chatInput.value);
    });

    chatInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            sendQuery(chatInput.value);
        }
    });

    // Event listeners for quick chips
    chipBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            const query = btn.getAttribute("data-query");
            sendQuery(query);
        });
    });
});
