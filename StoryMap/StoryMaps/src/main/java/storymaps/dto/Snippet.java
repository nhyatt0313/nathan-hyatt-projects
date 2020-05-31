package storymaps.dao;

public class Snippet {
    
    private int id;
    private String storyId;
    private String name;
    private String content;
    private int lastSnippetId;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getStoryId() {
        return storyId;
    }

    public void setStoryId(String storyId) {
        this.storyId = storyId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public int getLastSnippetId() {
        return lastSnippetId;
    }

    public void setLastSnippetId(int lastSnippetId) {
        this.lastSnippetId = lastSnippetId;
    }
}
